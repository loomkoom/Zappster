const emailBtn = document.querySelector('#email_radio')
const emailField = document.querySelector('#email_field')
const postBtn = document.querySelector('#post_radio')
const postField = document.querySelector('#post_field')

$('#submitBtn').click(function () {
    /* when the button in the form, display the entered values in the modal */
    $('td#sender').html($('input#sender').val());
    $('td#receiver').html($('input#receiver').val());
    $('td#message').html($('textarea#message').val());
});

$('#submit').click(function () {
    /* when the submit button in the modal is clicked, submit the form */
    if (emailBtn.checked) {
        $('input#send_method').val('email');
        $('input#send_destination').val($('input#email_input').val());
    }
    if (postBtn.checked) {
        $('input#send_method').val('post');
        $('input#send_destination').val($('input#post_input').val());
    }
    $( '#wish_form' ).submit()
});

function checkSendMethod() {
    if (emailBtn.checked) {
        console.log('email checked')
        emailField.style.display = 'block';
    } else {
        emailField.style.display = 'none';
    }
    if (postBtn.checked) {
        console.log('post checked')
        postField.style.display = 'block';
    } else {
        postField.style.display = 'none';
    }
}

