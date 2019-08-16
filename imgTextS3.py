import boto3

if __name__ == "__main__":

    
    bucket='naveen-imgpro'
    photo='car1.jpg'
    s3 = boto3.client('s3')
    s3.upload_file(photo,bucket,photo)

    client=boto3.client('rekognition')

  
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
    textDetections=response['TextDetections']
    
    for text in textDetections:
            print (text['DetectedText'])
            # print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            #print ('Id: {}'.format(text['Id']))
            #if 'ParentId' in text:
            #    print ('Parent Id: {}'.format(text['ParentId']))
            #print ('Type:' + text['Type'])
            #print
