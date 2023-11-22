<template>
  <div class="container">
    <!-- Jumbotron -->
    <div class="jumbotron text-center rounded p-4 mb-4" style="background-color: #4a90e2; color: white;">
      <h1 class="display-4">Bank Radar</h1>
      <p class="lead">
        당신을 위한 저축 상품을 찾고 있는 레이더의 모습을 형상화하였어요. 이 레이더는 당신의 마음에 활력을 불어넣어줄 여행지까지 찾아준답니다.
      </p>
    </div>

    <!-- Main Service Section -->
    <div class="row mb-4">
      <div class="col-md-4">
        <div class="card rounded">
          <div class="card-body">
            <h5 class="card-title">여행을 즐기는 사람들</h5>
            <p class="card-text">여행을 즐기면서 돈을 아끼고 싶어하는 분들을 위해 Bank Radar가 특별한 저축 상품을 제안해요.</p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card rounded">
          <div class="card-body">
            <h5 class="card-title">신뢰할 만한 투자자</h5>
            <p class="card-text">신뢰할 만한 금융 상품을 찾고 싶어하는 투자자들을 위해 Bank Radar가 검증된 적금 상품을 추천해줘요.</p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card rounded">
          <div class="card-body">
            <h5 class="card-title">여행을 꿈꾸는 사람들</h5>
            <p class="card-text">적금이 만기를 맞은 후 여행을 꿈꾸는 분들을 위해, Bank Radar가 여행지 추천을 도와줘요.</p>
          </div>
        </div>
      </div>
    </div>

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

    <!-- Footer -->
    <footer class="footer text-white rounded p-4" style="background-color: #4a90e2; text-align: center;">
      Bank Radar는 여행 목표와 금융 목표가 조화를 이룰 수 있도록, 맞춤형 금융 조언과 여행 추천을 제공하고 있어요. 여행을 꿈꾸면서 동시에 저축을 하며, 목표를 이룰 수 있도록 돕는 게 Bank Radar의 목표입니다.
    </footer>
  </div>
</template>

<script setup>
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';


</script>

<style scoped>
/* 페이지 특정 스타일은 여기에 추가 */
.row {
  margin-left: -15px;
  margin-right: -15px;
}

.card {
  margin-bottom: 2rem;
}

.carousel-item img {
  height: 400px;
  object-fit: cover;
}

.jumbotron,
.carousel,
.footer {
  border-radius: 15px;
}

body {
  background-image: url('@/assets/test1.png'); /* 이미지의 경로로 변경하세요 */
  background-size: cover; /* 화면에 꽉 차도록 배경 이미지 크기 조절 */
  background-position: center; /* 이미지를 화면 가운데로 정렬 */
  background-repeat: no-repeat; /* 이미지 반복 없이 한 번만 표시 */
}
</style>
