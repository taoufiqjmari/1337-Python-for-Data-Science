def ft_tqdm(lst: range) -> None:
    total = len(lst)
    width = 106

    def print_progress(iteration):
        percent = f"{int(100 * (iteration / total))}"
        filled_length = int(width * iteration // total)
        bar = '█' * filled_length + ' ' * (width - filled_length - 1)
        print(f"\r{percent}%|{bar}| {iteration}/{total}", end='', flush=True)

    for i, item in enumerate(lst):
        yield item
        print_progress(i + 1)
