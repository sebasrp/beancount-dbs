import csv
import click
import beancount_dbs.dbs as dbs


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
def beancount_dbs_cli():
    click.echo("Hello world!")

@click.command()
@click.option(
    "--console",
    default=True,
    is_flag=True,
    help="Output info to stdout/console",
    show_default=True,
)
@click.option(
    "--csv",
    "csv_",
    default=False,
    is_flag=True,
    help="Output info to csv",
    show_default=True,
)
def cli(filename, csv_, console):
    print(f"Hellow worls")
    dbsImporter = dbs()
    output = dbsImporter.identify(filename)

    if csv_:
        write_output_to_disk(output)

    if console:
        print(f"output: {output}")


def write_output_to_disk(output, filename="output.csv"):
    header_names = [
        "transaction_date",
        "description",
        "amount",
        "credit",
    ]
    with open(filename, "w") as out:
        writer = csv.DictWriter(out, fieldnames=header_names, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for entry in output:
            writer.writerow(
                {
                    "transaction_date": entry.date,
                    "description": entry.description,
                    "amount": entry.amount,
                    "credit": entry.credit,
                }
            )
    print(f"...Successfully created {filename}.")


if __name__ == "__main__":
    cli()