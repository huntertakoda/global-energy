package etl_opt

import (
	"encoding/csv"
	"fmt"
	"os"
	"strings"
)

// run handles the etl optimization process

func Run(inputFilePath, outputFilePath string) error {
	fmt.Println("starting etl optimization...")

	// open input file

	inputFile, err := os.Open(inputFilePath)
	if err != nil {
		return fmt.Errorf("failed to open input file: %w", err)
	}
	defer inputFile.Close()

	// create output file

	outputFile, err := os.Create(outputFilePath)
	if err != nil {
		return fmt.Errorf("failed to create output file: %w", err)
	}
	defer outputFile.Close()

	// read and process input file

	reader := csv.NewReader(inputFile)
	writer := csv.NewWriter(outputFile)
	defer writer.Flush()

	reader.LazyQuotes = true // handle bare quotes
	reader.TrimLeadingSpace = true

	lineNumber := 0
	validRecords := 0

	for {
		lineNumber++
		record, err := reader.Read()

		// handle eof gracefully

		if err != nil {
			if err.Error() == "EOF" {
				break
			}
			fmt.Printf("skipping problematic row on line %d: %v (error: %v)\n", lineNumber, record, err)
			continue
		}

		// sanitize fields: remove bare quotes or invalid characters

		for i, field := range record {
			record[i] = strings.ReplaceAll(field, `"`, "") // remove bare quotes
			record[i] = strings.TrimSpace(record[i])       // trim leading/trailing spaces
		}

		// skip rows with empty fields

		if len(record) == 0 || strings.Join(record, "") == "" {
			fmt.Printf("skipping empty or invalid row on line %d\n", lineNumber)
			continue
		}

		// write valid record to the output file

		if err := writer.Write(record); err != nil {
			fmt.Printf("failed to write row on line %d: %v\n", lineNumber, err)
			continue
		}
		validRecords++
	}

	// check if there are any valid records

	if validRecords == 0 {
		return fmt.Errorf("no valid records found in the input file")
	}

	fmt.Printf("etl optimization completed successfully. valid records: %d\n", validRecords)
	fmt.Println("output saved to:", outputFilePath)
	return nil
}
