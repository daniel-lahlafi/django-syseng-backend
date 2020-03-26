var toolkits;


window.onload = function() {
  fetch("http://localhost:8000/api/get-toolkit-names")
    .then(res => {
      return res.json();
    })
    .then(jsonData => {
      toolkits = jsonData.toolkit_names
      updateToolkitList()
      
    })
    .catch(err => {
      console.log(err)
    })
}

function updateToolkitList(filter="") {
  let quizListContainer = document.getElementById("quiz-list")

  quizListContainer.innerHTML = "";

  toolkits.forEach(name => {
    if (!name.toLowerCase().includes(filter)) {
      console.log("here")
      return;
    }


    let listItem = document.createElement("li")
    let quizList = document.createElement("div")
    quizList.onclick = function() {
      let lists = quizListContainer.querySelectorAll("li")
      lists.forEach(li => {li.className = ""})
      listItem.className = "active"
      
      loadQuiz(name)
    }
    quizList.className = "quizlist"
    let quizItem = document.createElement("div")
    quizItem.className = "quizlist__details--name"
    let quizName = document.createElement("div")
    quizName.className = "quiz_name"
    quizName.innerHTML = name
    quizItem.appendChild(quizName)
    
    quizList.appendChild(quizItem)
    listItem.appendChild(quizList)
    quizListContainer.appendChild(listItem)
  });
}

function filterToolkits() {
  let toolkit = document.getElementById("toolkit-search").value
  updateToolkitList(toolkit.toLowerCase())
  
  
}



function loadQuiz(toolkit_name) {
    const quizContainer = document.getElementById('quizcontainer');
    const previousButton = document.getElementById("previous");
    const nextButton = document.getElementById("next");
    const submitButton = document.getElementById('submit');
    const resultsContainer = document.getElementById('results');
    let currentSlide = 0;
    let questions = [];
    let slides = [];

    fetch("http://localhost:8000/api/quiz/" + toolkit_name)
        .then(res => {
            return res.json();
        })
        .then(loadedQuestions => {
            questions = loadedQuestions.result;
            buildQuiz();
            
        })
        .catch(err => {
            console.error(err);
        });

        buildQuiz= () => {
            
            
            // variable to store the HTML output
            const output = [];
        
            // for each question...
            questions.forEach(
              (currentQuestion, questionNumber) => {
        
                // variable to store the list of possible answers
                const answers = [];
        
                // and for each available answer...
                  // ...add an HTML radio button
                  answers.push(
                    `<label id="${questionNumber}1" class= "answer1">
                      <input type="radio" name="question${questionNumber}" value="${1}">
                      <span class="radio-style1">${1} :
                      ${currentQuestion.answer_1}</span>
                    </label>`
                  );
                  answers.push(
                    `<label id="${questionNumber}2" class= "answer2">
                      <input type="radio" name="question${questionNumber}" value="${2}">
                      <span class="radio-style2">${2} :
                      ${currentQuestion.answer_2}</span>
                    </label>`
                  );
                  answers.push(
                    `<label id="${questionNumber}3" class= "answer3">
                      <input type="radio" name="question${questionNumber}" value="${3}">
                      <span class="radio-style3">${3} :
                      ${currentQuestion.answer_3}</span>
                    </label>`
                  );
                  answers.push(
                    `<label id="${questionNumber}4" class= "answer4">
                      <input type="radio" name="question${questionNumber}" value="${4}">
                      <span class="radio-style4">${4} :
                      ${currentQuestion.answer_4}</span>
                    </label>`
                  );
        
                // add this question and its answers to the output
                output.push(
                  `<div class="slide">
                    <div class="question"> ${currentQuestion["question"]} </div>
                    <div class="answers"> ${answers.join("")} </div>
                  </div>`
                );
              }
            );

            // finally combine our output list into one string of HTML and put it on the page
            quizContainer.innerHTML = output.join('');
            slides = document.querySelectorAll(".slide");
            showSlide(currentSlide);
          }
          
          function showResults(){

            // gather answer containers from our quiz
            const answerContainers = quizContainer.querySelectorAll('.answers');
        
            // keep track of user's answers
            let numCorrect = 0;
        
            // for each question...
            questions.forEach( (currentQuestion, questionNumber) => {
              // find selected answer
              const answerContainer = answerContainers[questionNumber];
              const selector = `input[name=question${questionNumber}]:checked`;
              const userAnswer = (answerContainer.querySelector(selector) || {}).value;

              // if answer is correct
              if(userAnswer == currentQuestion.correct_answer){
                // add to the number of correct answers
                numCorrect++;
                // color the answers green
                for (let i = 1; i < 5; i++) {
                  if (i == userAnswer) {
                    document.getElementById(`${questionNumber}${userAnswer}`).style.color = 'lightgreen'
                  } else {
                    document.getElementById(`${questionNumber}${i}`).style.color = 'red'
                  }
                }

              }
              // if answer is wrong or blank
              else{
                // color the answers red
                answerContainers[questionNumber].style.color = 'red';
                correctAnswer = currentQuestion.correct_answer;

                for (let i = 1; i < 5; i++) {
                  if (i == correctAnswer) {
                    document.getElementById(`${questionNumber}${correctAnswer}`).style.color = 'lightgreen'
                  } else {
                    document.getElementById(`${questionNumber}${i}`).style.color = 'red'
                  }
                }
              }
            });
        
            // show number of correct answers out of total
            resultsContainer.innerHTML = `${numCorrect} out of ${questions.length}`;
          }

          function showSlide(n) {
            slides[currentSlide].classList.remove('active-slide');
            slides[n].classList.add('active-slide');
            currentSlide = n;
            if(currentSlide === 0){
                previousButton.style.display = 'none';
              }
            else{
                previousButton.style.display = 'inline-block';
            }
            if(currentSlide === slides.length-1){
                nextButton.style.display = 'none';
                submitButton.style.display = 'inline-block';
            }
            else{
                nextButton.style.display = 'inline-block';
                submitButton.style.display = 'none';
            }
          }
        
          function showNextSlide() {
            showSlide(currentSlide + 1);
          }
        
          function showPreviousSlide() {
            showSlide(currentSlide - 1);
          }

        previousButton.addEventListener("click", showPreviousSlide);
        nextButton.addEventListener("click", showNextSlide);
        submitButton.addEventListener('click', showResults);
          
}
