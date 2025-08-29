import pandas as pd


def modify(
    df: pd.DataFrame,
    num_of_rows: int,
    tradables_only: bool,
    min_price: int = 250000
) -> pd.DataFrame:
    """
    Process a FIFA player dataset and return the top players by market value.

    Steps performed:
    - Convert 'ExternalPrice' to numeric, dropping invalid entries.
    - Optionally filter out untradeable players if `tradables_only` is True.
    - Keep only rows where 'ExternalPrice' is greater than `min_price`.
    - Select 'Name', 'Rating', 'ExternalPrice', and 'Discard Value' columns.
    - Rename 'ExternalPrice' to 'Value'.
    - Sort players by 'Value' in descending order.
    - Reset the index to start from 1.
    - Return the top `num_of_rows` rows.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing player data.
    num_of_rows : int
        Number of rows to return.
    tradables_only : bool
        Whether to include only tradable players (exclude untradeables).
    min_price : int, optional
        Minimum value threshold for 'ExternalPrice'. Defaults to 250000.

    Returns
    -------
    pd.DataFrame
        Processed DataFrame containing the top `num_of_rows` players by value.
    """

    df['ExternalPrice'] = pd.to_numeric(df['ExternalPrice'], errors='coerce')

    if tradables_only:
        df = df[df["Untradeable"] == False]

    df = df[df['ExternalPrice'] > min_price]

    # keep relevant columns
    cols = ["Name", "Rating", "ExternalPrice"]
    if "Discard Value" in df.columns:
        cols.append("Discard Value")

    df = df[cols]

    df = df.rename(columns={"ExternalPrice": "Value"})
    df = df.sort_values(by="Value", ascending=False)
    df = df.reset_index(drop=True)
    df.index = df.index + 1

    return df.head(num_of_rows)
