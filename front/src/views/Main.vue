<template>
    <div>
  <div class="container">
    <!-- Jumbotron -->
    <section class="jumbotron text-center rounded p-4 m-3 section" style="background-color: aliceblue; color: black;">
      <div class="container">
        <h1 class="display-4">Bank Radar</h1>
      <p class="lead">
        당신을 위한 저축 상품을 찾고 있는 레이더의 모습을 형상화하였어요. <br>
        레이더는 당신의 마음에 활력을 불어넣어줄 여행지까지 찾아준답니다.
      </p>
    </div>
    </section>

    <!-- Carousel -->
    <div id="carouselExampleAutoplaying" class="carousel slide mb-3" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
            <img src="https://images.pexels.com/photos/1004584/pexels-photo-1004584.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
            <img src="https://images.pexels.com/photos/1285625/pexels-photo-1285625.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
            <img src="https://images.pexels.com/photos/2087391/pexels-photo-2087391.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
            <img src="https://images.pexels.com/photos/417344/pexels-photo-417344.jpeg" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
            <img src="https://images.pexels.com/photos/441379/pexels-photo-441379.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
            <img src="https://images.pexels.com/photos/161401/fushimi-inari-taisha-shrine-kyoto-japan-temple-161401.jpeg" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
            <img src="https://images.pexels.com/photos/1121782/pexels-photo-1121782.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" class="d-block w-100" alt="...">
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>

      <!-- Main Service Section -->
      <div class="row custom-style-cardbox">
        <h3 class="card-header text-center">이런 사람들에게 추천해요!</h3>

        <div class="col-md-4 mb-4">
          <div class="card border rounded h-100 custom-style-card">
            <div class="card-body">
              <h5 class="card-title">💸 여행을 원하지만 비용 걱정으로 망설이는 사람들</h5>
              <p class="card-text">여행은 하고 싶지만 비용 때문에 망설이는 분들을 위해,<br>
                여행 비용과 적금 상품을 추천하여 여행 계획을 지원해드려요.</p>
            </div>
          </div>
        </div>

        <div class="col-md-4 mb-4">
          <div class="card border rounded h-100 custom-style-card">
            <div class="card-body">
              <h5 class="card-title">🌍 여행을 위해 돈을 모으는 최적의 방법</h5>
              <p class="card-text">여행을 위해 적금이 필요한 분들을 위해,<br>
                특별한 저축 상품을 제안해요.</p>
            </div>
          </div>
        </div>

        <div class="col-md-4 mb-4">
          <div class="card border rounded h-100 custom-style-card">
            <div class="card-body">
              <h5 class="card-title">🌟 적금 만기 후 여행을 계획하는 사람들</h5>
              <p class="card-text">적금이 만기를 맞은 후 여행을 꿈꾸는 분들을 위해,<br>
                여행지 추천을 도와줘요.</p>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>


<script setup>
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';


</script>

<style scoped>
/* 페이지 특정 스타일은 여기에 추가 */
.custom-style-cardbox {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  background-color: aliceblue;
  padding: 20px;
  border-radius: 15px;
}

.custom-style-card {
  border: none;
}
.custom-style-card:hover {
  border: 3px solid #3E4095; /* 테두리 색상 변경 */
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3); /* 그림자 효과 추가 */
  transform: scale(1.05); /* 크기 약간 늘리기 */
}

.custom-style-card .card-body {
  text-align: center;
}

.custom-style-card .card-title {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 1rem;
  height: 30%;
}

.custom-style-card .card-text {
  font-size: 1rem;
}

.card-header {
  color: black;
  margin-bottom: 10px;
  font-weight: bold;
}

.jumbotron,
.carousel,
.footer {
  border-radius: 15px;
}
</style>
