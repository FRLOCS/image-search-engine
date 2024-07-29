from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)



    #randomGif = random.choice(myGifs)

    #return render_template('gifs.html', random=randomGif, myGifs=myGifs)

recently_search = []

@app.route('/input', methods=["GET", "POST"])
def input():
    imgData = {
        "dogs": ["https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_3x2.jpg", "https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*", "https://d3544la1u8djza.cloudfront.net/APHI/Blog/2021/07-06/small+white+fluffy+dog+smiling+at+the+camera+in+close-up-min.jpg", "https://paradepets.com/.image/t_share/MTkxMzY1Nzg4NjczMzIwNTQ2/cutest-dog-breeds-jpg.jpg", "https://spca.bc.ca/wp-content/uploads/2023/06/happy-samoyed-dog-outdoors-in-summer-field.jpg", "https://www.akc.org/wp-content/uploads/2018/05/Three-Australian-Shepherd-puppies-sitting-in-a-field.jpg"],
        "cats": ["https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg", "https://www.wfla.com/wp-content/uploads/sites/71/2023/05/GettyImages-1389862392.jpg?w=2560&h=1440&crop=1", "https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/advisor/wp-content/uploads/2023/09/how-much-does-a-cat-cost.jpeg.jpg", "https://i.natgeofe.com/n/4cebbf38-5df4-4ed0-864a-4ebeb64d33a4/NationalGeographic_1468962.jpg", "https://images.theconversation.com/files/168121/original/file-20170505-1693-ymh4bc.jpg?ixlib=rb-4.1.0&q=45&auto=format&w=926&fit=clip", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/800px-Juvenile_Ragdoll.jpg"],
        "cat gifs": ["https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnF2bjR6b2U1cjR6bGhmZ2o4MWVyNzI4YjN3MTRzYjF6cnU3eW11NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/E5tUBlZsw7WNO/giphy.webp", "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnBkNDljOHBpaTl1NmI3cTdsN2swMHF3NXBrdXhoN2x6cXF5ZG5jeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hCAze4yGkNbsk/giphy.webp",   "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjllaG9qbDB0ZTQyOWFuYTlvMWdjNXc1YjNnamFxcGliZjgxMHVzYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4vZehSoIvGdMc/giphy.webp","https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExanFzeGpwdGFlbm42bHRpd3hvbzM0dTIwZTIybnVzZmlyZWdwNjNobSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gHR6htUKuzGAo/giphy.webp"],
        "paintings": {"https://paintingandframe.com/art-imgs/frida_kahlo/self_portrait_dedicated_to_dr_eloesser_1940-13559s250.jpg","https://i.pinimg.com/originals/46/e2/66/46e26655d54b8efba4ce043512b623e3.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGv6-JTKNwJYf7dEC5mzfyQMmMjQ7LmMbb2w&s", "https://m.media-amazon.com/images/I/71KC-JjKlxL._AC_UF894,1000_QL80_.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1200px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg", "https://cdn.britannica.com/46/198846-050-82EE84FC/Lady-Ermine-oil-panel-Leonardo-da-Vinci.jpg"},
        "celebrities": {"https://people.com/thmb/y-A6cZ_B8rdGQwTDDVG4aHzNXos=/4000x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(689x399:691x401)/lebron-james-7f070c722a1143e295b46f67ff0005dc.jpg","https://cached.imagescaler.hbpl.co.uk/resize/scaleWidth/1272/cached.offlinehbpl.hbpl.co.uk/news/ORP/Kanye_4.jpg","https://www.usmagazine.com/wp-content/uploads/2023/03/Billie-Eilish-more-celebrities-who-took-social-media-breaks-social.jpg?w=1000&quality=86&strip=all", "https://www.byrdie.com/thmb/MIe01J86hMfPU4JL7UQIrAyMokc=/1500x0/filters:no_upscale():max_bytes(200000):strip_icc()/Celebrities-NEWS-Mobile-24276ccc3c8643adb45380e088435a37.jpg", "https://manofmany.com/wp-content/uploads/2019/12/2019s-Most-Influential-Male-Celebrities-Under-30-According-To-Forbes-6.jpg", "https://media.voguebusiness.com/photos/650dbecd12de6c737bc18493/3:2/w_1998,h_1332,c_limit/CELEBRITY-MARKETING-vogue-business-story.jpg"},
        "scenery": {"https://thumbs.dreamstime.com/blog/2021/02/how-to-create-stunning-images-ordinary-sceneries-landscape-photography-36969-image103752677.jpg", "https://cioviews.com/wp-content/uploads/2020/12/2-2.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvN61QhfxmiBYIbO3an3_PoLp1PG0a1euK6Ug-C1fz7Y58cUZx7Nfuoo5l4c-Ej3D9Dog&usqp=CAU", "https://image-tc.galaxy.tf/wijpeg-9gkc4d23uujayacsg1pnirf1v/delicate-arch_standard.jpg?crop=164%2C0%2C1184%2C888"},
        "cartoons": {"https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2018/09/1200/675/1c1efe99-the-simpsons-660-ap.jpg?ve=1&tl=1", "https://preview.redd.it/best-cartoon-of-all-time-v0-i4ye37u0owhb1.jpg?width=640&crop=smart&auto=webp&s=8613171a3848d8c376da3dd61bdff9a9cf7516f1", "https://assets.nick.com/uri/mgid:arc:imageassetref:shared.nick.us:3abfa1f3-dc7f-4137-9ac2-57c18b50bd67?quality=0.7&gen=ntrn", "https://static1.colliderimages.com/wordpress/wp-content/uploads/2022/01/Episodes-of-Nostalgic-Nickelodeon-Cartoons.jpg"},
        "beaches": {"https://hips.hearstapps.com/hmg-prod/images/champagne-beach-espiritu-santo-island-vanuatu-royalty-free-image-1655672510.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdIJQNVPLMiQWiY8J9fzyoM_h89tFeyE0lYw&s", "https://upload.wikimedia.org/wikipedia/commons/7/73/Beach_at_Fort_Lauderdale.jpg", "https://worlds50beaches.com/assets/images/world-2024/011.webp"},
        "movies": {"https://www.rd.com/wp-content/uploads/2019/09/shutterstock_editorial_5884766b-e1569251332374.jpg", "https://images.bauerhosting.com/legacy/media/6140/b515/4699/e01c/48f2/7735/inside-out-main2.jpg?ar=16%3A9&fit=crop&crop=top&auto=format&w=1440&q=80", "https://parade.com/.image/t_share/MTkwNTc4NzcxNjE5NjIwNzMy/disney-pixar.jpg", "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_.jpg", "https://resizing.flixster.com/ySiX7RlyKRuuxCcAI7SgdkMAZ0U=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzc4ZmJhZjZiLTEzNWMtNDIwOC1hYzU1LTgwZjE3ZjQzNTdiNy5qcGc="},
        "oakland": {"https://drupal8-prod.visitcalifornia.com/sites/drupal8-prod.visitcalifornia.com/files/vc_spotlightoakland_hero_oakland_rf_895763984_1280x640.jpg", "https://cdn.britannica.com/75/64475-050-CF6FE1CB/Oakland-California.jpg", "https://media-cdn.tripadvisor.com/media/photo-s/02/2a/20/4d/oakland-skyline.jpg", "https://assets.goaaa.com/image/upload/w_auto,q_auto:best,f_auto/v1647564541/singularity-migrated-images/View-downtown-weekend-in-oakland-via-magazine.jpg.jpg", "https://media.timeout.com/images/105241394/image.jpg"}
        }
    
    if request.method == 'POST':
        query = request.form['query']
        if query not in imgData:
            return "Nothing found for " + query
        recently_search.append(query)
        return render_template('result.html', imgData=imgData[query], count=len(imgData[query]))
    return render_template('input.html', url=url_for('input'), recently_search=recently_search)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
