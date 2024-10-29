from anticaptchaofficial.recaptchav3proxyless import *
import requests

def do_login(captcha_key):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8,it;q=0.7,fr;q=0.6',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        'user_name': EMAIL,
        'password': PASSWORD,
        'recaptcha_token': captcha_key,
        'device': {
            'udid': '2e93d9e9b5093350fba2f05db58c1012476c7e10b40aac48720a9246c1ea9a32',
            'os': 'windows-10',
            'browser': 'chrome',
        },
    }

    response_dict = requests.post('https://gestiontv.vodafone.es/api/users/sign_in', headers=headers, json=json_data).json()
    print(f"response_dict delete_device_login ---> {response_dict}")
    return response_dict.get('status') == 'ok'


def get_captcha():
    solver = recaptchaV3Proxyless()
    solver.set_verbose(1)
    solver.set_key(API_KEY)
    solver.set_website_url("https://gestiontv.vodafone.es/login")
    solver.set_website_key("6LeoxW4dAAAAAJTBQhUIl9KMOo0HMv2qInjLpq_k")
    solver.set_min_score(0.9)

    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        if isinstance(g_response, dict) and g_response.get('status') in ['error', 'unauthorized', 'recaptcha_failed']:
            print(f"Error obtaining captcha: {g_response}")
            return None
        return g_response
    else:
        print(f'Error obtaining captcha: {solver.error_code}')
        return None


def main():
    captcha_key = get_captcha()
    if captcha_key:
        do_login(captcha_key)

main()