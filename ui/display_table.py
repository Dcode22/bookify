def print_table(table_headers, rows):
    col_widths = [len(header) for header in table_headers]
    
    for row in rows:
        for i, field in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(field)))
    
    header_row = ' | '.join(header.ljust(col_widths[i]) for i, header in enumerate(table_headers))
    separator_row = '-+-'.join('-' * col_widths[i] for i in range(len(table_headers)))
    
    print(separator_row)
    print(header_row)
    print(separator_row)

    for row in rows:
        data_row = ' | '.join(truncate_field(str(field)).ljust(col_widths[i]) for i, field in enumerate(row))
        print(data_row)
        print(separator_row)

def truncate_field(field):
    if len(field) > 45:
        return field[:42] + '...'
    return field
