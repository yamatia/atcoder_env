import os,sys,re
from posix import listdir
import subprocess
import shutil

"""
引数で、実行ファイルのパス、実行するもの(test or sub)、実行言語
ex)
python3 /workspaces/atcoder_test/scripts/oj.py /workspaces/atcoder_test/test/test.py /workspaces/atcoder_test/ test pypy
python3 /workspaces/atcoder_test/scripts/oj.py /workspaces/atcoder_test/test/test.py /workspaces/atcoder_test/ submit pypy 
"""
def read_url(file_path):
    with open(file_path,mode='r') as f:
        file_text = f.readlines()
    
    problem_url = re.match(r"URL:(.*)",file_text[1]).group(1)

    return problem_url

def oj_download(problem_url,file_path,workspace_path,problem_id):
    # workspace/sapmle/*に10個以上のサンプルフォルダあるようなら不要なので削除する
    sample_dir = os.path.join(workspace_path,'sample/')
    
    dirs = []
    for dir in os.listdir(sample_dir):
        dir_path = os.path.join(sample_dir,dir)
        if os.path.isdir(dir_path):
            dirs.append((dir_path,os.path.getctime(dir_path)))
    
    if len(dirs)>10:
        dirs.sort(key=lambda x:x[1],reverse=True)
        for i in range(10,len(dirs)):
            shutil.rmtree(dirs[i][0])
            
    # 問題が既にダウンロード済みかどうか
    problem_dir = os.path.join(workspace_path,'sample/',problem_id)
    
    # サンプルダウンロード済みなら処理スキップする
    if os.path.isdir(problem_dir):
        return problem_dir
    
    else:
        os.makedirs(problem_dir,exist_ok=True)
        cp = subprocess.run(['oj','d',problem_url,'--format','{}/sample-%i.%e'.format(problem_dir)])
        if cp.returncode!=0:
            print('oj download failed. exit')
            sys.exit(1)

        return problem_dir

def oj_test(problem_dir,file_path,run_language):
    if run_language=='python3':
        cp = subprocess.run(['oj','t','-c','python3 {}'.format(file_path),'-d',problem_dir,'-D','--print-memory'])
       
    elif run_language=='pypy3':
        cp = subprocess.run(['oj','t','-c','pypy3 {}'.format(file_path),'-d',problem_dir,'-D','--print-memory'])
        
    elif run_language=='cpp':
        cp = subprocess.run(['g++',sys.argv[1],'-o','./a.out'])
        cp = subprocess.run(['oj','t','-c','./a.out','-d',problem_dir,'-i','--print-memory'])
        os.remove('./a.out')
        
    else:
        print('Can not test this language..')
    
    return

def oj_submit(problem_url,file_path,run_language):
    pypy_id = '4047'
    if run_language=='python3':
        cp = subprocess.run(['oj','submit','--wait=0','--yes',problem_url,file_path])
    elif run_language=='pypy3':
        cp = subprocess.run(['oj','submit','--wait=0','--yes','--no-guess','--language',pypy_id,problem_url,file_path])

def main():
    file_path = sys.argv[1]
    workspace_path = sys.argv[2]
    run_type = sys.argv[3]
    run_language = sys.argv[4]
    
    problem_url = read_url(file_path)
    problem_id = os.path.splitext(os.path.basename(problem_url))[0]
    
    print('RUN_type:',run_type)
    if run_type=='test':
        problem_dir = oj_download(problem_url,file_path,workspace_path,problem_id)
        oj_test(problem_dir,file_path,run_language)
             
    elif run_type=='submit':
        oj_submit(problem_url,file_path,run_language)
    
    
    
if __name__=='__main__':
    main()