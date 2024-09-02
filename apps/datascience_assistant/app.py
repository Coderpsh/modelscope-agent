import os
import sys

import streamlit as st

os.environ['DASHSCOPE_API_KEY'] = 'sk-ec2073251be949c8b47015e4e9cec61a'


def setup_project_paths():
    current_dir = os.path.dirname(os.path.abspath(__file__))  # noqa
    project_root_path = os.path.abspath(os.path.join(current_dir,
                                                     '../../'))  # noqa
    sys.path.append(project_root_path)  # noqa


if __name__ == '__main__':
    setup_project_paths()
    from modelscope_agent.agents.data_science_assistant import \
        DataScienceAssistant  # noqa
    from modelscope_agent.tools.metagpt_tools.tool_recommend import \
        TypeMatchToolRecommender  # noqa

    st.title('数据分析助理')
    st.write(
        '我是你的数据分析小助手，帮助你执行数据科学相关的任务~'
    )
    st.write(
        '请上传您需要处理的数据文件并输入您的问题'
    )

    files = st.file_uploader(
        '请上传文件', accept_multiple_files=True)
    last_file_name = ''
    user_request = st.text_area('提问')
    if st.button('提交'):
        llm_config = {
            'model': 'qwen2-72b-instruct',
            'model_server': 'dashscope',
        }
        # 创建数据分析助手角色
        data_science_assistant = DataScienceAssistant(
            llm=llm_config,
            tool_recommender=TypeMatchToolRecommender(tools=['<all>']))
        for file in files:
            with open(file.name, 'wb') as f:
                f.write(file.getbuffer())

        # 回答用户问题
        data_science_assistant.run(user_request=user_request, streamlit=True)
