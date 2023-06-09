// Логика открытия фильтра
const buttonsOpenAccordeon = document.querySelectorAll('.accordion__button');

Array.from(buttonsOpenAccordeon).forEach((item) => {
  item.addEventListener('click', function (evt) {
    evt.target.classList.toggle('accordion__button_open')
    const accordeonContent = item.closest('.accordion__item').lastElementChild;

    accordeonContent.classList.toggle('accordion__content_open');

    if (!accordeonContent.classList.contains('accordion__content_open')) {
      accordeonContent.style.maxHeight = null;
    } else {
      accordeonContent.style.maxHeight = null;
      accordeonContent.style.maxHeight = accordeonContent.scrollHeight + 'px'
    }
  })
})

// Логика модального окна
const eventItem = document.querySelector('.section__link');
const popupEvent = document.querySelector('.popup_event');
const popupAuth = document.querySelector('.popup_auth');
const closeButton = document.querySelector('.popup__close');
const authButton = document.querySelector('.header__image-button');

eventItem.addEventListener('click', (evt) => {
  evt.preventDefault();
  popupEvent.classList.add('popup_opened');
})

authButton.addEventListener('click', () => {
  popupAuth.classList.add('popup_opened');
})

popupAuth.addEventListener('click', (evt) => {
  if (evt.target.className == 'popup__close-pic') {
    console.log(evt.target.className)
    popupAuth.classList.remove('popup_opened');
  }
})

popupEvent.addEventListener('click', (evt) => {
  console.log(evt.target.className);
  if (evt.target.className == 'popup__close-pic') {
    popupEvent.classList.remove('popup_opened');
  }
})