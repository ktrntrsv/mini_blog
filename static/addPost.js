
const button = document.querySelector("#showCreatePostForm")
const form = document.querySelector("#CreatePostForm")

button.addEventListener("click", function (e){
   showForm()
})

form.addEventListener("submit", function (e){
    e.preventDefault()

    const closeButton = e.target.querySelector("#hidePostForm")

    let userName = e.target.querySelector('[name="username"]').value
    let csrf = e.target.querySelector('[name="csrf_token"]').value
    let $post = e.target.querySelector('[name="post"]')
    let post = $post.value

    closeButton.addEventListener("click", function (e){
        hideForm($post)
    })

    const params = new URLSearchParams()
    params.append("csrf_token", csrf)
    params.append("post", post)

   axios.post('/user/'+ userName + '/create_post/', params)
       .then(function (resp){
            hideForm($post)
       })
       .catch(function (err){
           hideForm($post)
           alert("возникла ошибка" + err)
       })
})

function showForm(){
    form.style.display = "block"
    button.style.display = "none"
}

function hideForm($post){
    form.style.display = "none"
    button.style.display = "block"
    $post.value = ""
}