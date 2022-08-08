    (function loop() {
            setTimeout(function () {
                var posts = new XMLHttpRequest();
                posts.open( "GET", "http://127.0.0.1:8000/api/v1/posts/", false ); // false for synchronous request
                posts.send( null );
                var post = JSON.parse(posts.responseText);
                    for (let i = 0; i < post.length; i++) {

                        try {
                          document.getElementById("pt_" + post[i].id).innerHTML = post[i].title;
                          document.getElementById("pb_" + post[i].id).innerHTML = post[i].body;
                        }

                        catch (e) {
                            i++
                        }

                    }
                loop()
            }, 5000);
        }());