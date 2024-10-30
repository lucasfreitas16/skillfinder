import boto3
import os


client = boto3.client ("s3",
    aws_access_key_id="",
    aws_secret_access_key="",
    aws_session_token="",
    region_name='eu-west-1',
    )


#resp = client.list_buckets()
#print(resp)

bucket_name = 'armskillfinder'
#refix_ = 'Vagas1/'
#ocal_directory = '../teste2/'

def S3download(Prefix_, Local_directory):
    response = client.list_objects_v2(Bucket=bucket_name, Prefix=Prefix_)
    #if not os.path.exists(Local_directory):
        #os.makedirs(Local_directory)
    
    if 'Contents' in response:
        for obj in response['Contents']:
        # Obtendo o nome do objeto
            object_key = obj['Key']
            if object_key == Prefix_:
                continue

        # Criando o caminho local para salvar o arquivo
            local_filename = os.path.join(Local_directory, os.path.basename(object_key))

        # Baixando o arquivo               
            client.download_file(bucket_name, object_key, local_filename)
            print(f"Arquivo {object_key} baixado com sucesso para {local_filename}.")
    else:
        print("Nenhum objeto encontrado.")
        
#folder_name = 'Analise01/Curriculos/'
#file_name = 'mic mic - projeto.pdf'
#file_path = '/home/ubuntu/environment/teste3/mic mic - projeto.pdf'        
        
def S3envio(file_path, folder_name, file_name):  
   
    
    # Concatena a pasta ao nome do arquivo
    client.upload_file(file_path, bucket_name, folder_name + file_name)
    
    print(f'{file_name} foi enviado para {folder_name} no bucket {bucket_name}')




  #client.download_file("armazenskillfinder","Teste1/curriculo-1.pdf", "/downloaded-curriculo1.pdf"),

#3(Prefix_,Local_directory)
