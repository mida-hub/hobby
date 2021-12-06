use clap::{App, Arg};
use std::fs::File;
use std::io::{stdin, BufRead, BufReader};

fn main() {
    let matches = App::new("My RPN program")
                    .version("1.0.0")
                    .author("Your name")
                    .about("Super awesome sample RPN calculator")
                    .arg(
                        Arg::new("formula_file")
                            .about("Formulas written in RPN")
                            .value_name("FILE")
                            .index(1)
                            .required(false),
                    )
                    .arg(
                        Arg::new("verbose")
                            .about("Sets the level of verbosity")
                            .short('v')
                            .long("verbose")
                            .required(false),
                    )
                    .get_matches();
    let verbose = matches.is_present("verbose");
    match matches.value_of("formula_file"){
        Some(file) => {
            let f = File::open(file).unwrap();
            let reader = BufReader::new(f);

            run(reader, verbose)
        }
        None => {
            let stdin = stdin();
            let reader = stdin.lock();
            run(reader, verbose);
        }
    }
}

fn run<R: BufRead>(reader: R, verbose: bool) {
    for line in reader.lines() {
        let line = line.unwrap();
        println!("{}", line);
    }
}
