CSTORE_GET_SPEC = {
    'tags': ['편의점'],
    'description': '특정 편의점 점포 조회, 기본적으로는 페이지 기반의 점포 조회를 실행하며, 쿼리를 통한 고급 검색 가능',
    'parameters': [
        {
            'name': 'store_band',
            'description': '점포의 브랜드 이름 (CU: cu, GS25: gs25, 세븐일레븐: 7eleven)',
            'in': 'query',
            'type': 'str',
            'required': False
        },

        {
            'name': 'store_name',
            'description': '점포의 이름 (CU가로수길점, 파주출판단지점)',
            'in': 'query',
            'type': 'str',
            'required': False
        },

        {
            'name': 'store_address',
            'description': '점포의 도로명 주소 (EX: 대전광역시 동구 용운로, 서울특별시 용산구 ... 등등)',
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

        {
            'name': 'target_lng',
            'description': '위치 기반 조회를 위한 현재 사용자의 위치 정보 중 경도값',
            'in': 'query',
            'type': 'float',
            'required': False
        },

        {
            'name': 'target_lat',
            'description': '위치 기반 조회를 위한 현재 사용자의 위치 정보 중 위도값',
            'in': 'query',
            'type': 'float',
            'required': False
        },

        {
            'name': 'target_radius',
            'description': '위치 기반 조회를 위한 현재 사용자의 미터 단위 탐색 반경',
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
                        "id": "5af29bffa9378e11e47bd92c",
                        "brand": "7eleven",
                        "name": "간성읍점",
                        "address": "강원도 고성군 간성로 39-2",
                        "location": [
                            128.470461,
                            38.3789797
                        ],
                        "tel": "010-6274-7146"
                    },

                    {
                        "id": "5af29c00a9378e11e47bd92d",
                        "brand": "7eleven",
                        "name": "강대사거리점",
                        "address": "강원도 춘천시 백령로 1381층 편의점",
                        "location": [
                            127.7424175,
                            37.8721907
                        ],
                        "tel": "033-241-8769"
                    },

                    {
                        "id": "5af29c01a9378e11e47bd92e",
                        "brand": "7eleven",
                        "name": "강대천하점",
                        "address": "강원도 춘천시 백령로75 (효자동) 1층",
                        "location": [
                            127.7423861,
                            37.8706505
                        ],
                        "tel": "033-255-0922"
                    },

                    {
                        "id": "5af29c01a9378e11e47bd92f",
                        "brand": "7eleven",
                        "name": "강릉5주공점",
                        "address": "강원도 강릉시 월대산로 431층 102호",
                        "location": [
                            128.9166617,
                            37.7599484
                        ],
                        "tel": None
                    },

                    {
                        "id": "5af29c02a9378e11e47bd930",
                        "brand": "7eleven",
                        "name": "강릉경강로점",
                        "address": "강원도 강릉시 경강로2258  (포남동)",
                        "location": [
                            128.9078407,
                            37.7748552
                        ],
                        "tel": "033-645-5455"
                    }
                ]
            }
        }
    }
}
