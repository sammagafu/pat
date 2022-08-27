<template>
<section class="breadcrumb-header">
  <div class="overlay"></div>
  <div class="container">
    <div class="row">
      <div class="col-lg-6">
        <div class="banner">
          <h1>Contact Us</h1>
          <ul>
            <li>
              <a href="/" class="router-link-active">Home</a>
            </li>
            <li>
              <i class="fas fa-angle-right" aria-hidden="true"></i>
            </li>
            <li>Contact Us</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="contact-us py-100">
  <div class="container">
    <div class="contact-info-content">
      <div class="row">
        <div class="col-md-6 col-lg-4">
          <div class="contact-box">
            <i class="flaticon-call"></i>
            <div class="box">
              <a class="phone" href="tel:+255767029904">+255 767 029 904</a>
              <a class="phone" href="tel:+255754047857">+255 754 047 857</a>
            </div>
          </div>
        </div>
        <div class="col-md-6 col-lg-4">
          <div class="contact-box">
            <i class="flaticon-email"></i>
            <div class="box">
              <a class="mail" href="mailto:info@pediatrics.or.tz">info@pediatrics.or.tz</a>
              <a class="mail" href="mailto:tjacob@pediatrics.or.tz">tjacob@pediatrics.or.tz</a>
            </div>
          </div>
        </div>
        <div class="col-md-6 col-lg-4">
          <div class="contact-box">
            <i class="flaticon-location"></i>
            <div class="box">
              <p>4TH FLOOR PAEDIATRIC COMPLEX, Muhimbili, Dar es Salaam</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-6">
        <div class="map-box">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d495.21610815529425!2d39.27398200988829!3d-6.802802353850062!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x185c4b8ee07d7087%3A0xe435d3ef3b945b8!2sPaediatric%20Ward!5e0!3m2!1sen!2stz!4v1658928937449!5m2!1sen!2stz" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="add-comments">
          <form class="inner-add-comments form-contact-2">
            <div class="row">
              <div class="col-md-6 inner-add-comments-box">
                <input type="text" name="name" placeholder="Name" required="">
              </div>
              <div class="col-md-6 inner-add-comments-box">
                <input type="Email" name="email" placeholder="Email" required="">
              </div>
              <div class="col-md-12 inner-add-comments-box">
                <input type="text" name="subj" placeholder="Subject" required="">
              </div>
              <div class="col-md-12 inner-add-comments-box">
                <textarea name="message" placeholder="Your Message Here" required=""></textarea>
              </div>
              <div class="col-md-12 inner-add-comments-box last">
                <button type="submit" class="btn-1">Submit</button>
                <span class="out-message m-2"></span>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
</template>