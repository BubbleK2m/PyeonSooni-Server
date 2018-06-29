PRODUCT_GET_SPEC = {
    'tags': ['상품'],
    'description': '특정 브랜드의 상품 조회, 기본적으로는 페이지 기반의 상품 조회를 실행하며, 쿼리를 통한 고급 검색 가능',
    'parameters': [
        {
            'name': 'product_band',
            'description': '상품의 브랜드 이름 (CU: cu, GS25: gs25, 세븐일레븐: 7eleven)',
            'in': 'query',
            'type': 'str',
            'required': False
        },

        {
            'name': 'product_name',
            'description': '상품의 이름 (진한스누피커피우유, 참치마요삼각김밥)',
            'in': 'query',
            'type': 'str',
            'required': False
        },

        {
            'product': 'product_name',
            'description': '상품의 특정 행사 진행여부를 확인할 수 있는 플래그 (0: 행사 X, -1: 행사 상품, 1: 1 + 1, 2: 2 + 1)',
            'in': 'query',
            'type': 'str',
            'required': False
        },

        {
            'name': 'page_index',
            'description': '페이지 기반 조회를 위한 현재 사용자의 위치 정보 중 현재 페이지의 인덱스 (기본값 1)',
            'in': 'query',
            'type': 'int',
            'required': False
        },

        {
            'name': 'page_length',
            'description': '페이지 기반 조회를 위한 현재 사용자의 위치 정보 중 조회하고자 하는 페이지의 길이 (기본값 5)',
            'in': 'query',
            'type': 'int',
            'required': False
        },
    ],

    'responses': {
        '200': {
            'description': '성공',
            'examples': {
                'application/json': [
                    {
                        "id": "5af29d6ea9378e2804cec73f",
                        "brand": "7eleven",
                        "name": "맛있는행복)아몬드고구마샐러드",
                        "price": 2200,
                        "flag": None,
                        "image": "http://www.7-eleven.co.kr/upload/product/8805684/004885.1.jpg"
                    },

                    {
                        "id": "5af29d6ea9378e2804cec740",
                        "brand": "7eleven",
                        "name": "맛있는행복)콘샐러드110g",
                        "price": 2200,
                        "flag": None,
                        "image": "http://www.7-eleven.co.kr/upload/product/8805684/004892.1.jpg"
                    },

                    {
                        "id": "5af29d6ea9378e2804cec741",
                        "brand": "7eleven",
                        "name": "맛있는행복)망고푸딩220g",
                        "price": 2200,
                        "flag": None,
                        "image": "http://www.7-eleven.co.kr/upload/product/8805684/004915.1.jpg"
                    },

                    {
                        "id": "5af29d6ea9378e2804cec742",
                        "brand": "7eleven",
                        "name": "맛있는행복)사과푸딩220g",
                        "price": 2200,
                        "flag": None,
                        "image": "http://www.7-eleven.co.kr/upload/product/8805684/004908.1.jpg"
                    },

                    {
                        "id": "5af29d6ea9378e2804cec743",
                        "brand": "7eleven",
                        "name": "PB)와라샤인쿨자두180ml",
                        "price": 300,
                        "flag": None,
                        "image": "http://www.7-eleven.co.kr/upload/product/8806371/302741.1.jpg"
                    }
                ]
            }
        }
    }
}
