def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(lst)
    width = 50  # Could be change to whatever width wanted for the bar

    def showcase(i):
        percent = f"{100 * i // total}"
        filled = width * i // total
        bar = '█' * filled + ' ' * (width - filled)
        print(f"\r{percent}%|{bar}| {i}/{total}", end='')

    for i in range(total):
        yield i
        showcase(i + 1)
