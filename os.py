import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Dataset loading
mnist = input_data.read_data_sets("./samples/MNIST_data/", one_hot=True) #데이터를 다운로드 한다

# Set up model
x = tf.placeholder(tf.float32, [None, 784]) # TensorFlow에게 계산을 하도록 명령할 때 입력할 값, 각 이미지들은 784차원의 벡터
W = tf.Variable(tf.zeros([784, 10])) # 784차원의 이미지 벡터를 곱하여 10차원 벡터의 증거를 만들것
b = tf.Variable(tf.zeros([10])) # 출력에 더하기 위한 값
y = tf.nn.softmax(tf.matmul(x, W) + b) # tf.matmul(x, W) 표현식으로 xx 와 WW를 곱하고, 그것에 b를 더하여 tf.nn.softmax를 적용한다.

y_ = tf.placeholder(tf.float32, [None, 10]) # 정답을 입력하기 위한 새 placeholder

cross_entropy = -tf.reduce_sum(y_*tf.log(y)) #  교차 엔트로피를 구현한다
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy) # TensorFlow에게 학습도를 0.01로 준 경사 하강법(gradient descent) 알고리즘을 이용하여 교차 엔트로피를 최소화

# Session
init = tf.initialize_all_variables() #만든 변수들을 초기화

sess = tf.Session() # 모델을 시작하고
sess.run(init) #  변수들을 초기화

# Learning
for i in range(1000): # 학습을1000번 시킨다
  batch_xs, batch_ys = mnist.train.next_batch(100) # 학습 세트로부터 100개의 무작위 데이터들의 일괄 처리(batch)들을 가져온다
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys}) # placeholders를 대체하기 위한 일괄 처리 데이터에 train_step 피딩을 실행

# Validation
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1)) # tf.argmax(y,1)과 tf.argmax(y_,1)이 맞는지 tf.equal을 이요해서 확인해본다.
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) # 부정소숫점으로 캐스팅한 후 평균값을 구한다

# Result should be approximately 91%.
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})) #전확도를 확인해본다.
