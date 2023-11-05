from pathlib import Path

from website import Website


_INDEX_HTML = '''<html>
    <head>
        <title>Brain Computer Interface</title>
    </head>
    <body>
        <ul>
            {users}
        </ul>
    </body>
</html>
'''
_USER_LINE_HTML = '''
<li><a href="/users/{user_id}">user {user_id}</a></li>
'''
_USER_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface: User {user}</title>
    </head>
    <body>
        <table>
            {thoughts}
        </table>
    </body>
</html>
'''
_USER_THOUGHT_HTML = '''
<tr>
    <td>{time}</td>
    <td>{thought}</td>
</tr>
'''


def run_webserver(address, data_dir):
    website = Website()
    data_dir = Path(data_dir)

    @website.route('/')
    def index():
        users = set([user.name for user in data_dir.iterdir()])
        users_html = list()
        for user_dir in users:
            users_html.append(_USER_LINE_HTML.format(user_id=user_dir))
        index_html = _INDEX_HTML.format(users='\n'.join(users_html))
        return 200, index_html

    @website.route('/users/([0-9]+)')
    def user(user_id):
        users = set([user.name for user in data_dir.iterdir()])
        if user_id not in users:
            return 404, ''
        thoughts_html = list()
        for file in (data_dir / user_id).iterdir():
            date, hour = file.name.split('.')[0].split('_')
            time = ' '.join([date, hour.replace('-', ':')])
            thought = file.read_text()
            thoughts_html.append(_USER_THOUGHT_HTML.format(time=time, thought=thought))
        user_html = _USER_HTML.format(user=user_id, thoughts='\n'.join(thoughts_html))
        return 200, user_html

    website.run(address)


if __name__ == '__main__':
    run_webserver(('127.0.0.1', 8000), 'data/')
