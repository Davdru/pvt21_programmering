from rich.console import Console
from rich.table import Table


table = Table(title="Björn tabell")
table.add_column("Ticker", justify="right", style="cyan")
table.add_column("Date", style="cyan")
table.add_column("Closing", style="green")

table.add_row("ABB", "2021-10-07", "[green]255.1[/green]")
table.add_row("ABB", "2021-10-08", "[red]255.1[/red]")

console = Console()
console.print(table)
