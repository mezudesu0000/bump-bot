import discord

def patch_bot_py():
    dir = "/".join(discord.__path__[0].replace("\\", "/").split("/")[:-1])
    bot_py_path = f"{dir}/discord/ext/commands/bot.py"
    try:
        with open(bot_py_path, "r", encoding="utf_8") as f:
            code = f.read()

        target = "if self._skip_check(message.author.id, self.user.id):  # type: ignore"
        if target not in code:
            print("パッチ適用済み")
            return

        try:
            delete = (
                target + code.split(target)[1].split("return ctx")[0] + "return ctx"
            )
        except IndexError:
            print("ファイルが破損しているか既に適用済み")
            return

        code = code.replace(delete, "")
        with open(bot_py_path, "w", encoding="utf_8") as f:
            f.write(code)
        print("パッチを適用しました")

    except Exception as e:
        if "list index out of range" in str(e):
            print("list index out of range → パッチ済みとして無視")
        else:
            print(f"処理中にエラーが発生しました：{e}")

if __name__ == "__main__":
    patch_bot_py()