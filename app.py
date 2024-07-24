from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)



    #randomGif = random.choice(myGifs)

    #return render_template('gifs.html', random=randomGif, myGifs=myGifs)


@app.route('/input', methods=["GET", "POST"])
def input():
    imgData = {
        "dogs": ["https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_3x2.jpg", "https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*", "https://d3544la1u8djza.cloudfront.net/APHI/Blog/2021/07-06/small+white+fluffy+dog+smiling+at+the+camera+in+close-up-min.jpg", "https://paradepets.com/.image/t_share/MTkxMzY1Nzg4NjczMzIwNTQ2/cutest-dog-breeds-jpg.jpg", "https://spca.bc.ca/wp-content/uploads/2023/06/happy-samoyed-dog-outdoors-in-summer-field.jpg"],
        "cats": ["https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg", "https://www.wfla.com/wp-content/uploads/sites/71/2023/05/GettyImages-1389862392.jpg?w=2560&h=1440&crop=1", "https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/advisor/wp-content/uploads/2023/09/how-much-does-a-cat-cost.jpeg.jpg", "https://i.natgeofe.com/n/4cebbf38-5df4-4ed0-864a-4ebeb64d33a4/NationalGeographic_1468962.jpg", "https://images.theconversation.com/files/168121/original/file-20170505-1693-ymh4bc.jpg?ixlib=rb-4.1.0&q=45&auto=format&w=926&fit=clip"],
        "gifs": ["https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnF2bjR6b2U1cjR6bGhmZ2o4MWVyNzI4YjN3MTRzYjF6cnU3eW11NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/E5tUBlZsw7WNO/giphy.webp", "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnBkNDljOHBpaTl1NmI3cTdsN2swMHF3NXBrdXhoN2x6cXF5ZG5jeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hCAze4yGkNbsk/giphy.webp",   "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjllaG9qbDB0ZTQyOWFuYTlvMWdjNXc1YjNnamFxcGliZjgxMHVzYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4vZehSoIvGdMc/giphy.webp","https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExanFzeGpwdGFlbm42bHRpd3hvbzM0dTIwZTIybnVzZmlyZWdwNjNobSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gHR6htUKuzGAo/giphy.webp"]
        }
    
  
    if request.method == 'POST':
        query = request.form['query']
        if query not in imgData:
            return "Nothing found for " + query
        return render_template('result.html', imgData=imgData[query], count=len(imgData[query]))
    return render_template('input.html', url=url_for('input'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
