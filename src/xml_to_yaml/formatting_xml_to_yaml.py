# 파일명 찐빠나서 변경 할거면 run.py 내에서 선언도 변경을 해야 한다

import xmltodict
import yaml
import json
"""
추후 하고싶은 것 메모
가독성이 생각보다 별로라서, 데이터 별로 줄바꿈이 있으면 좋겠음

이걸 ecu에 활용할 일이 있을지는 모르겠지만, 쓸거면 모든 데이터를 クォーテーション으로 감쌀 필요가 있어 보인다 << 귀찮아 보이는군


"""


def convert_xml_to_yaml(xml_file, yaml_file):
    """XML 파일을 읽어 YAML 파일로 변환하여 저장합니다."""

    # 1. XML 파일을 읽어 파이썬 딕셔너리(Dictionary)로 변환
    with open(xml_file, 'r', encoding='utf-8') as f:
        xml_string = f.read()

    data_dict = xmltodict.parse(xml_string)

    # (선택) 변환된 딕셔너리 구조 중간 확인
    # print(json.dumps(data_dict, indent=2, ensure_ascii=False))

    # 2. 딕셔너리를 YAML 형식의 문자열로 변환
    # allow_unicode=True: 한글 등 깨지지 않게 처리
    # sort_keys=False: 원래 순서 유지
    yaml_string = yaml.dump(data_dict, allow_unicode=True, sort_keys=False, indent=2)

    # 3. YAML 문자열을 파일로 저장
    with open(yaml_file, 'w', encoding='utf-8') as f:
        f.write(yaml_string)

    print(f"✅ 변환 완료: '{xml_file}' -> '{yaml_file}'")

if __name__ == '__main__':
    convert_xml_to_yaml('my_data.xml', 'my_data_from_python.yaml')