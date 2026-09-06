"""Keep observed DEER point selection independent of author fit availability."""
import math

def extract_numeric_rows(cells, columns, start=5, stop=3000):
    """Return source row ids and numeric values for exactly the declared role."""
    ids, rows = [], []
    for index in range(start, stop):
        values = [cells.get(column+str(index)) for column in columns]
        if all(value and value.get('type') == 'n' for value in values):
            row = [float(value['value']) for value in values]
            if not all(map(math.isfinite, row)):
                raise ValueError('NONFINITE_SOURCE_OBSERVATION')
            ids.append(index)
            rows.append(row)
    return ids, rows

def extract_processed_roles(cells, time_column, observed_column, fit_column):
    observed_ids, observed = extract_numeric_rows(cells, [time_column, observed_column])
    fit_ids, fit = extract_numeric_rows(cells, [time_column, fit_column])
    old_ids, _ = extract_numeric_rows(cells, [time_column, observed_column, fit_column])
    return dict(processed=observed, fit_audit=fit,
        selection_audit=dict(observed_rows=observed_ids, fit_rows=fit_ids,
            old_coupled_rows=old_ids,
            previously_excluded_observed_rows=sorted(set(observed_ids)-set(old_ids)),
            observed_last_time=observed[-1][0] if observed else None,
            old_last_time=next((row[0] for index,row in reversed(list(zip(observed_ids,observed))) if index in old_ids), None)))
