package ingestion

import (
	"encoding/csv"
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
)

// run handles the data ingestion process

func Run(url, filePath string) error {
	fmt.Println("starting data ingestion...")

	// ensure the directory exists

	dir := filepath.Dir(filePath)
	if err := os.MkdirAll(dir, os.ModePerm); err != nil {
		return fmt.Errorf("failed to create directory: %w", err)
	}

	// download data

	if err := downloadData(url, filePath); err != nil {
		return fmt.Errorf("data ingestion failed: %w", err)
	}

	// validate data

	if err := validateData(filePath); err != nil {
		return fmt.Errorf("data validation failed: %w", err)
	}

	fmt.Println("data ingestion completed successfully.")
	return nil
}

// downloadData fetches data from a url and saves it locally

func downloadData(url, filePath string) error {
	fmt.Println("downloading data from:", url)

	// http get request

	resp, err := http.Get(url)
	if err != nil {
		return fmt.Errorf("failed to download data: %w", err)
	}
	defer resp.Body.Close()

	// create file

	file, err := os.Create(filePath)
	if err != nil {
		return fmt.Errorf("failed to create file: %w", err)
	}
	defer file.Close()

	// save data to file

	_, err = io.Copy(file, resp.Body)
	if err != nil {
		return fmt.Errorf("failed to save data: %w", err)
	}

	fmt.Println("data saved to:", filePath)
	return nil
}

// validateData ensures the downloaded file is a valid csv and skips problematic rows

func validateData(filePath string) error {
	fmt.Println("validating downloaded data...")

	// open file

	file, err := os.Open(filePath)
	if err != nil {
		return fmt.Errorf("failed to open file: %w", err)
	}
	defer file.Close()

	// read csv content

	reader := csv.NewReader(file)
	reader.LazyQuotes = true // allow lenient handling of quotes
	reader.TrimLeadingSpace = true

	// validate rows

	lineNumber := 0
	validRecords := 0
	for {
		lineNumber++
		record, err := reader.Read()
		if err != nil {
			// handle eof gracefully

			if err == io.EOF {
				break
			}

			// log and skip rows with field count errors or any other parsing issues

			fmt.Printf("skipping problematic row on line %d: %v (error: %v)\n", lineNumber, record, err)
			continue
		}

		// skip empty rows

		if len(record) == 0 {
			fmt.Printf("skipping empty row on line %d\n", lineNumber)
			continue
		}

		// count valid records

		validRecords++
	}

	// check if there are any valid records

	if validRecords == 0 {
		return fmt.Errorf("no valid records found in the file")
	}

	fmt.Printf("data validation completed successfully. valid records: %d\n", validRecords)
	return nil
}
