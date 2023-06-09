// Логика открытия фильтра
const buttonsOpenAccordeon = document.querySelectorAll('.accordion__button');

Array.from(buttonsOpenAccordeon).forEach((item) => {
  item.addEventListener('click', function (evt) {
    evt.target.classList.toggle('accordion__button_open');
    const accordeonContent = item.closest('.accordion__item').lastElementChild;

    accordeonContent.classList.toggle('accordion__content_open');

    if (!accordeonContent.classList.contains('accordion__content_open')) {
      accordeonContent.style.maxHeight = null;
    } else {
      accordeonContent.style.maxHeight = null;
      accordeonContent.style.maxHeight = accordeonContent.scrollHeight + 'px';
    }
  });
});

// Логика модального окна
const eventItems = document.querySelectorAll('.section__link');
const popupEvent = document.querySelector('.popup_event');
const popupAuth = document.querySelector('.popup_auth');
const closeButton = document.querySelector('.popup__close');
const authButton = document.querySelector('.header__image-button');

eventItems.forEach((eventItem, index) => {
  eventItem.addEventListener('click', (evt) => {
    evt.preventDefault();
    const selectedTitle = evt.currentTarget.querySelector(
      '.section__item-title'
    );
    const selectedEvent = eventsArray.find(
      (event) => selectedTitle.textContent === event.title
    );
    popupEvent.querySelector('.popup__title').textContent = selectedEvent.title;
    popupEvent.querySelector('.popup__list').innerHTML = `
      <li class="popup__item">Возраст: ${selectedEvent.age}</li>
      <li class="popup__item">Место проведения: ${selectedEvent.location}</li>
      <li class="popup__item">Время начала: ${selectedEvent.startTime}</li>
    `;
    popupEvent.querySelector('p').textContent = selectedEvent.description;
    popupEvent.querySelector(
      '.popup__price'
    ).textContent = `Стоимость: ${selectedEvent.price} рублей`;
    popupEvent.querySelector(
      '.popup__date'
    ).textContent = `До начала мероприятия: ${selectedEvent.daysLeft} дней`;

    popupEvent.classList.add('popup_opened');
  });
});

authButton.addEventListener('click', () => {
  popupAuth.classList.add('popup_opened');
});

popupAuth.addEventListener('click', (evt) => {
  if (evt.target.className == 'popup__close-pic') {
    console.log(evt.target.className);
    popupAuth.classList.remove('popup_opened');
  }
});

popupEvent.addEventListener('click', (evt) => {
  if (evt.target.className == 'popup__close-pic') {
    popupEvent.classList.remove('popup_opened');
  }
});
