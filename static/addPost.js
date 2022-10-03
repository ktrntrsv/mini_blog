const writeButton = document.querySelector("#showCreatePostForm")
const form = document.querySelector("#CreatePostForm")

writeButton.addEventListener("click", function (e) {
    showForm()
})

form.addEventListener("submit", function (e) {
    e.preventDefault()

    const closeButton = e.target.querySelector("#hidePostForm")

    closeButton.addEventListener("click", function (e) {
        hideForm($post)
    })

    let userName = e.target.querySelector('[name="username"]').value
    let csrf = e.target.querySelector('[name="csrf_token"]').value
    let $post = e.target.querySelector('[name="post"]')
    let post = $post.value

    const params = new URLSearchParams()
    params.append("csrf_token", csrf)
    params.append("post", post)

    axios.post('/user/' + userName + '/create_post/', params)
        .then(function (resp) {
            hideForm($post)
        })
        .catch(function (err) {
            hideForm($post)
            alert("Error" + err)
        })
})

function showForm() {
    form.style.display = "block"
    writeButton.style.display = "none"
}

function hideForm($post) {
    form.style.display = "none"
    writeButton.style.display = "block"
    $post.value = ""
}