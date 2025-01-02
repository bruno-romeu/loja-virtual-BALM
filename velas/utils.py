import requests 

def calcular_frete_melhor_envio(cep_origem, cep_destino, peso, altura, diâmetro, circunferência):
    url = "https://www.melhorenvio.com.br/api/v2/me/shipment/calculate"
    headers = {
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNzk0ODRhMjk5ZDVkZTJmMzgwZGMyNGVmYzdlOWI1YWE1ZThjMzk4MjdkNjI1YTY5M2U3OTIxNGUzZGUxNGNlZmExZTllYzEzYTVjYTU2ZTciLCJpYXQiOjE3MzU4MzYwODYuMzE0MDg5LCJuYmYiOjE3MzU4MzYwODYuMzE0MDksImV4cCI6MTc2NzM3MjA4Ni4yOTc3NjcsInN1YiI6IjlkZGY5M2MyLTdjZTQtNGRjYS05OWYxLTFlYzM5MjhkMjJkMSIsInNjb3BlcyI6WyJjYXJ0LXJlYWQiLCJjYXJ0LXdyaXRlIiwiY29tcGFuaWVzLXJlYWQiLCJjb21wYW5pZXMtd3JpdGUiLCJjb3Vwb25zLXJlYWQiLCJjb3Vwb25zLXdyaXRlIiwibm90aWZpY2F0aW9ucy1yZWFkIiwib3JkZXJzLXJlYWQiLCJwcm9kdWN0cy1yZWFkIiwicHJvZHVjdHMtZGVzdHJveSIsInByb2R1Y3RzLXdyaXRlIiwicHVyY2hhc2VzLXJlYWQiLCJzaGlwcGluZy1jYWxjdWxhdGUiLCJzaGlwcGluZy1jYW5jZWwiLCJzaGlwcGluZy1jaGVja291dCIsInNoaXBwaW5nLWNvbXBhbmllcyIsInNoaXBwaW5nLWdlbmVyYXRlIiwic2hpcHBpbmctcHJldmlldyIsInNoaXBwaW5nLXByaW50Iiwic2hpcHBpbmctc2hhcmUiLCJzaGlwcGluZy10cmFja2luZyIsImVjb21tZXJjZS1zaGlwcGluZyIsInRyYW5zYWN0aW9ucy1yZWFkIiwidXNlcnMtcmVhZCIsInVzZXJzLXdyaXRlIiwid2ViaG9va3MtcmVhZCIsIndlYmhvb2tzLXdyaXRlIiwid2ViaG9va3MtZGVsZXRlIiwidGRlYWxlci13ZWJob29rIl19.ojdi8pJ9-Y308fZrfk1vKBVINXQhLHf4utkTW3sqYcIyLeKMvHzuTid_2ExTUQ8U2O_2tHiviZIHxkIEF77WtERMCNt0YmhKOmilypTS6cWX8_M5v90bm_0OpD5XLXQL9nEhCPMG2uWmyDyu_3B4F7r7OULth_qQHJxbDs_mLVZnZWvPOM2I_DeoiDYYwr12ZTQ1oqXJ7UXeNIQQ0F0a9sj8yJT6YH_pqcojMt8KepSaKo3vSjk_lz8Wc_qAiqAdJyoqDbbfRJ4lzhKlNHBLlPlglqMkbF_22s5Jdmk4NOfAieK3l4_4D_d2UTLuLG8O8vUip_PhjCA0Xxqnc9fUMl2NvfJVsQldBVOFSylplrCeNgXBhPYgk6KDxkZ3x7nxAXHByAgNcg6GNeJdtzvXgS0fC71ZDCD26qGEuBT0lNWipLY3Ahg3htvI9Q5gsS4y2Mvc62WNx-n19pXXTwig95NYi4rTg64J-98wObMpY2DxrfSmlRp_kZ5uZmcGmfO9D-dMQWlSIyFtmDGGTe71chB5gSYL_kmNF64T6DkPCo4BVXukt5paOUIQMRvr20P4TmIpfk9PrNDab_xMql95FqBE8p_r44VbCVy6SLby3EGVb4w94Ump2MX_Da4_CR9WpbuBjizk3BfCiETjem8Lt9vKjNDglGbIK02ixzeRu6s',

        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    data = {
        'from': {'postal_code': cep_origem},
        'to': {'postal_coce': cep_destino},
        'products':[
            {
                'weight': peso,
                'width': diâmetro,
                'height': circunferência,
                'length': altura,
                'quantity': 1
            }
        ],
        'services': ['SEDEX']
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code==200:
        return response.json()
    else:
        raise Exception(f'Erro na API Melhor Envio: {response.status_code} {response.text}')