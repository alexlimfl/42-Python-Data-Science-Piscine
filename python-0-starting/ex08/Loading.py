import shutil


def ft_tqdm(lst: range) -> None:
    """implementation of tqdm"""
    total = len(lst)
    prog_bar_w = shutil.get_terminal_size().columns - 40
    for i, item in enumerate(lst):
        progress = int(i / total * prog_bar_w)
        progress_percentage = int(progress / prog_bar_w * 100)
        progress_bar = f"|{'█' * progress:<{prog_bar_w}}|"
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        print(f"\r{progress_info}", end="", flush=True)
        yield item
    i += 1
    progress = int(i / total * prog_bar_w)
    progress_percentage = int(progress / prog_bar_w * 100)
    progress_bar = f"|{'█' * progress:<{prog_bar_w}}|"
    progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
    print(f"\r{progress_info}", end="", flush=True)
    yield item
