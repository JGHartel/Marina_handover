import pandas as pd
import requests
import time
import pandas as pd
from typing import List, Optional
import requests
import time
import pandas as pd
from pathlib import Path
from typing import List, Optional, Union
from tqdm import tqdm

FIELDS = ["id",
        "image_id",
        "title",
        "artist_display",
        "date_start",
        "is_public_domain"
        "dimensions",
        "dimensions_detail"
        "classification_titles",
]

QUERY = (
    'classification_titles:"painting" '
    'AND is_public_domain:true '
)

def fetch_metadata(
    fields: Optional[List[str]] = FIELDS,
    query: Optional[str] = QUERY,
    limit: int = 100,
    delay: float = 0.1,
    max_pages: Optional[int] = None,
    verbose: bool = True,
    output_file: Optional[Union[str, Path]] = None,
    overwrite: bool = False,
) -> pd.DataFrame:
    """
    Fetch artwork metadata from the Art Institute of Chicago API, with optional Lucene-style filtering.

    Args:
        fields: List of fields to request.
        classification_titles: Convenience shortcut for e.g. ['Painting'].
        query: Full Elasticsearch/Lucene query string (overrides classification_titles if given).
        ...
    """
    BASE_URL = "https://api.artic.edu/api/v1/artworks/search"

    if output_file is not None:
        output_file = Path(output_file)
        if output_file.exists() and not overwrite:
            if verbose:
                print(f"Loading existing file: {output_file}")
            return pd.read_pickle(output_file)
        
    params = {
        "query": query,
        "limit": limit,
        "fields": ",".join(fields),
        "page": 1,
    }

    # Fetch first page to estimate pagination
    resp = requests.get(BASE_URL, params=params)
    resp.raise_for_status()
    json_resp = resp.json()
    pagination = json_resp.get("pagination", {})
    total_pages = min(pagination.get("total_pages", 1), max_pages) if max_pages else pagination.get("total_pages", 1)

    all_data = []
    pbar = tqdm(total=total_pages, desc="Fetching artworks", unit="page")

    for page in range(1, total_pages + 1):
        params["page"] = page
        resp = requests.get(BASE_URL, params=params)
        if resp.status_code != 200:
            backoff_delay = 60
            print(f"Warning: Request for page {page} failed with status {resp.status_code}. Trying again in {backoff_delay} seconds.")
            time.sleep(backoff_delay)
            resp = requests.get(BASE_URL, params=params)

        all_data.extend(resp.json().get("data", []))
        pbar.update(1)
        time.sleep(delay)

    pbar.close()
    df = pd.DataFrame(all_data)

    if output_file:
        if output_file.suffix.lower() == '.json':
            df.to_json(output_file, orient='records', indent=2)
        else:
            df.to_pickle(output_file)
        if verbose:
            print(f"Saved {len(df)} entries to {output_file}")

    return df
