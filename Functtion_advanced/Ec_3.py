def sorting_cheeses(**kwargs):
    print(kwargs)
    sorted_cheeses = sorted(
        kwargs.items(),
        key=lambda x: (-len(x[1]), x[0]),
    )

    result = []

    for name, pieces in sorted_cheeses:
        result.append(name)
        result.extend(
            sorted(pieces, reverse=True)
        )
    return '\n'.join([str(x) for x in result])
