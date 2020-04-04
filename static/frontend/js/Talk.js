var is_confirming_answer = false;
var question = null
var attempt_counter = 0
var question_answer = null
var Words = document.getElementById("words");
var TalkWords = document.getElementById("talkwords");
var TalkSub = document.getElementById("talksub");
var toolkit_dropdown = document.getElementById('SelectedToolkit');
var randomResponse = new Array("Is there anything else I can help you?","What else can I help you?:)",":)","Hope that helps you:)","Please let me know if you need more help:)");

window.onload = function() {
/*---------------Initialise the List of Toolkit Names------------------------------------------------- */
    toolkit_dropdown.length = 0;
    let defaultOption = document.createElement('option');
    defaultOption.text = 'Choose Toolkit';
    toolkit_dropdown.add(defaultOption);
    toolkit_dropdown.selectedIndex = 0;
    const request_get_toolkit_names = new XMLHttpRequest();
    request_get_toolkit_names.open('GET','https://rcgp-chatbot.azurewebsites.net/api/get-toolkit-names',true);
    request_get_toolkit_names.onload = function() {
        if (this.status == 200){
            let data = JSON.parse(request_get_toolkit_names.responseText).toolkit_names;

            data.forEach(toolkit_name => {
                let option = document.createElement('option');
                option.text = toolkit_name;
                option.value = toolkit_name;
                toolkit_dropdown.add(option);
            });
        }
    }
    request_get_toolkit_names.onerror = function(){
        console.error('An error occurred fetching the JSON from' +'https://rcgp-chatbot.azurewebsites.net/api/get-toolkit-names')
    };
    request_get_toolkit_names.send()
  /* ----------------------------------------------------------------------------------------------------------------------*/  

    TalkSub.onclick = function() {
        if (TalkWords.value == "") {
            let str = '<li class="message received"><div class="message__text">Can\'t have an empty message</div></li>';
            Words.innerHTML = Words.innerHTML + str;
            window.scrollTo(0,document.body.scrollHeight);
            return;
        } else if (toolkit_dropdown.value == "Choose Toolkit") {
            let str = '<li class="message received"><div class="message__text">Please pick a toolkit before asking questions</div></li>';
            Words.innerHTML = Words.innerHTML + str;
            window.scrollTo(0,document.body.scrollHeight);

            return;
        }
        
        else {
            let str = '<li class="message sent"><div class="message__text">' + TalkWords.value + '</div></li>';
            Words.innerHTML = Words.innerHTML + str;
        }

        if (is_confirming_answer) {
            is_confirming_answer = false;
            if (TalkWords.value.toLowerCase().includes("no")) {
                attempt_counter += 1;
                sendRequest()
            } else {
                attempt_counter = 0;
                save_question()
            }
        } else {
            question = TalkWords.value
            sendRequest()
            
        }
        window.scrollTo(0,document.body.scrollHeight);


    }
}

function save_question() {
    $.ajax({
        type: "POST",
        url: '/api/questions/',   
        data: {
            csrfmiddlewaretoken: document.getElementById("csrf_token").value,
            question: question,
            toolkit: document.getElementById("SelectedToolkit").value,
            answer: question_answer
        },
        success:  function(response){
            answer = '<li class="message received"><div class="message__text">The answer has been saved for next time</div></li>';
            Words.innerHTML = Words.innerHTML + answer
        },
        error: function(xhr, ajaxOptions, thrownError) {
            answer = '<li class="message received"><div class="message__text">' + thrownError + '</div></li>';
            Words.innerHTML = Words.innerHTML + answer
        }
    });
    
}

function redirectToolkit() {
    toolkitName = toolkit_dropdown.value
    if (toolkitName == "Choose Toolkit") {
        let str = '<li class="message received"><div class="message__text">Please pick a toolkit first</div></li>';
        Words.innerHTML = Words.innerHTML + str;
        window.scrollTo(0,document.body.scrollHeight);
    } else {
        const request_get_toolkit_url = new XMLHttpRequest();
        request_get_toolkit_url.open('GET','https://rcgp-chatbot.azurewebsites.net/api/get-toolkit-url/'+toolkitName,true);
        request_get_toolkit_url.onload = function() {
            if (this.status == 200){
                let url = JSON.parse(request_get_toolkit_url.responseText).url;
                window.location.replace(url);
            }
        }
        request_get_toolkit_url.onerror = function(){
            let str = '<li class="message received"><div class="message__text">Error retrieving URL</div></li>';
            Words.innerHTML = Words.innerHTML + str;
            window.scrollTo(0,document.body.scrollHeight);
        };
        request_get_toolkit_url.send()
    }
}

function sendRequest() {
    input_box = document.getElementById("talkwords")
    document.getElementById("toggleModelAnn").click()

    $.ajax({
        type: "POST",
        url: '/api/search',   
        data: {
            csrfmiddlewaretoken: document.getElementById("csrf_token").value,
            question: question.toLowerCase().replace(/(!|'|\?)/g, ""),
            toolkit_name: document.getElementById("SelectedToolkit").value,
            attempt: attempt_counter
            },
        success:  function(response){
            let loading_animation = document.getElementById("loading");
            loading_animation.parentElement.removeChild(loading_animation)
    
            var answer = "";

            if (response.answer == "") {
                attempt_counter += 1;
                sendRequest();
                return;
            }

            // Attempt at sentiment analysis

            // if ((response.sentiment[0].label == 'NEGATIVE') && (response.sentiment[0].score > 0.8)) {
            //     comfort_response='<li class="message received"><div class="message__text">' + "I've noticed you are feeling upset with me I'll try do better" + '</div></li>'
            //     Words.innerHTML = Words.innerHTML + comfort_response;
            // }

            question_answer = response.answer
            answer = '<li class="message received"><div class="message__text">' + response.answer + '</div></li>';
            Words.innerHTML = Words.innerHTML + answer;
    
            if (response.answer = "") {
                attempt_counter += 1;
                sendRequest();
                return;
            }
    
            if (response.is_saved_answer == false) {
                check_answer();
            } else {
                humanlike_response()
            }
            
            TalkSub.disabled = false
            input_box.value = ""
            input_box.focus()
            document.getElementById("toggleModelAnn").click()


        },
        error: function(xhr, ajaxOptions, thrownError) {
            answer = '<li class="message received"><div class="message__text">'  + thrownError + '</div></li>';
            Words.innerHTML = Words.innerHTML + answer;
        }
    });



    Words.innerHTML = Words.innerHTML + '<li id="loading" class="message received"><div class="message__text"><div id="typing-loader"></div></div></li>'
    TalkSub.disabled = true
    input_box.value = ""
}

function check_answer() {
    Confirm = '<li class="message received"><div class="message__text">' +'Is the answer correct?'+ '</div></li>';
    Words.innerHTML = Words.innerHTML + Confirm;
    is_confirming_answer = true
}

function humanlike_response(){
    index = Math.floor((Math.random()*randomResponse.length))
    response_random = randomResponse[index]
    response = answer = '<li class="message received"><div class="message__text">'  + response_random + '</div></li>';
    Words.innerHTML = Words.innerHTML + response;
}