package edu.stanford.nlp.presidentialdebates.experiments;

import com.opencsv.CSVReader;
import edu.stanford.nlp.util.Execution;

import java.io.FileReader;

/**
 * Computes some summary statistics about a debate
 */
public class SummaryStatistics implements Runnable {

    @Execution.Option(gloss="Path to input file (as CSV)")
    String inputFilename;

    @Override
    public void run() {
        CSVReader reader = new CSVReader(new FileReader(inputFilename));
        String [] nextLine;
        while ((nextLine = reader.readNext()) != null) {
            // nextLine[] is an array of values from the line
            System.out.println(nextLine[0] + nextLine[1] + "etc...");
        }


    }


    public static void main(String[] args) {
        Execution.exec(new SummaryStatistics());
    }
}
