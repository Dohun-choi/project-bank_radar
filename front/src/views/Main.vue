<template>
    <div>
  <div class="container">
    <!-- Jumbotron -->
    <section class="jumbotron text-center rounded p-4 m-3 section" style="background-color: aliceblue; color: black;">
      <div class="container">
        <h1 class="display-4">Bank Radar</h1>
      <p class="lead">
        당신을 위한 저축 상품을 찾고 있는 레이더의 모습을 형상화하였어요. 레이더는 당신의 마음에 활력을 불어넣어줄 여행지까지 찾아준답니다.
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
    <div class="row card cardbox">
        <h3 class="card-header">이런 사람들에게 추천해요</h3>
        <div class="card rounded col-md-4 gx-3 px-3">
          <div class="card-body">
            <h5 class="card-title">여행을 즐기며 돈도 아끼는 특별한 방법을 찾는 사람들</h5>
            <p class="card-text">여행을 즐기면서 돈을 아끼고 싶어하는 분들을 위해 Bank Radar가 특별한 저축 상품을 제안해요.</p>
          </div>
        </div>
        <div class="card rounded col-md-4 gx-3 px3">
          <div class="card-body">
            <h5 class="card-title">적금 만기 후 여행을 계획하는 사람들</h5>
            <p class="card-text">적금이 만기를 맞은 후 여행을 꿈꾸는 분들을 위해, Bank Radar가 여행지 추천을 도와줘요.</p>
          </div>
      </div>
        <div class="card rounded col-md-4 gx-3 px3">
          <div class="card-body">
            <h5 class="card-title">여행을 원하지만 비용 걱정으로 망설이는 사람들</h5>
            <p class="card-text">여행은 하고 싶지만 비용 때문에 망설이는 분들을 위해, Bank Radar가 여행 비용과 적금 상품을 추천하여 여행 계획을 지원해드려요.</p>
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

.card {
    display: flex;
    flex-direction: row;
}

.section {
    background-color: #333;
    color: #fff;
    padding: 50px 0;
    text-align: center;
}

.section h2 {
    margin-bottom: 20px;
}

.section p {
    font-size: 18px;
    margin-bottom: 40px;
}

.btn-cta {
    background-color: #fff;
    color: #333;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    font-size: 16px;
}

.btn-cta:hover {
    background-color: #eee;
}
</style>
