# テスト用ファイル
import manager

if __name__ == "__main__":
    M = manager.Manager()
    M.input(file=True)
    M.ex4()
    M.print_info(detail=True)
    M.plot(save=True)
