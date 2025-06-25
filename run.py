# Gemini프롬프트에 이모지 사용해서 귀엽게 대답하라고 해놨더니 터미널 출력도 귀엽게 해 줌

from lib.formmating_xml_to_yaml import convert_xml_to_yaml
import os

"""
추후 하고 싶은 것 메모
formmating_xml_to_yaml.py 파일명이 오타났는데, 그거 수정하면 여기도 import 선언 수정 해야됨

main 함수 내 2. 부분
"""


def main(file_dir="./files/", save_dir="./files/"):
    """
    지정된 폴더(file_dir)에 있는 모든 .xml 파일을 찾아
    지정된 폴더(save_dir)에 .yaml 파일로 변환하여 저장합니다.
    """
    print(f"📁 작업 시작: '{os.path.abspath(file_dir)}' 폴더의 XML 파일을 변환합니다.")

    # 1. 대상 폴더의 모든 파일 목록을 가져옵니다.
    try:
        file_list = os.listdir(file_dir)
    except FileNotFoundError:
        print(f"❌ 오류: 폴더를 찾을 수 없습니다 -> '{os.path.abspath(file_dir)}'")
        return

    # 2. 각 파일을 순회하며 .xml 파일인지 확인하고 변환 작업을 수행합니다.
    # 였는데, 내가 쓰는 환경에서는 xml포맷 파일들의 확장자가 xml이 아니므로, 일단 yaml만 제외하고 트라이하도록 한 상황
    # Exception을 좀 세부화 하거나, 혹시 모를 오류 대비해서 아예 디렉토리나 yaml 같은 예외상황은 제외하도록 하면 좋을 것 같다

    for filename in file_list:
        if not filename.lower().endswith('.yaml'):
            # 입력될 XML 파일의 전체 경로
            source_xml_path = os.path.join(file_dir, filename)
            
            # 저장될 YAML 파일의 이름과 전체 경로 생성
            base_filename = os.path.splitext(filename)[0]
            save_yaml_path = os.path.join(save_dir, f"{base_filename}.yaml")

            try:
                # 3. 정의해둔 변환 함수를 호출합니다.
                convert_xml_to_yaml(source_xml_path, save_yaml_path)
            except Exception as e:
                # 변환 함수 실행 중 오류가 발생할 경우, 해당 파일은 건너뛰고 계속 진행합니다.
                print(f"❌ 오류 발생! '{filename}' 파일 변환 실패: {e}")
        else:
            # .yaml 파일은 건너뜁니다.
            print(f"  ⏩ '{filename}' 파일은 yaml이므로 건너뜁니다.")

    print("\n✨ 모든 작업이 완료되었습니다.")

if __name__ == "__main__":
    main(file_dir="./files/", save_dir="./files/")


# 이건 원래 썼던 파일 한 개 전용 코드인데, 입력 하나하나 하기 너무 귀찮아서 여러 개 한번에 적용 시키려고 AI딸깍 한 상황
# 현 시점엔 쓸 일이 딱히 없을 것 같아서 그냥 밑에 둔다
# 필요하면 함수화 하기
# import 는 위에 두개면 되니까 이것도

#def main(file_dir = "./files/", save_dir = "./files/"):
    #print(f"from_dir:{file_dir}, XMLファイル名を入力 例: my_data.xml")
    #file_path = input("xml_file :")
    #print(f"save_dir:{save_dir}, 保存するYamlファイル名. 例: output.yaml")
    #save_path = input("yaml_file:")

#    convert_xml_to_yaml(file_dir+file_path, save_dir+save_path)
    

#if __name__== "__main__":
#    main()
#####
