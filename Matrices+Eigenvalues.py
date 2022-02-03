from numpy import array, eye, matmul
from numpy.linalg import eig

def main():
  A = array([[0.8,0.3],[0.2, 0.7]])
  w,v = eig(A)
  print('First pair:',w[0], v[:,0])
  print('Second pair:', w[1], v[:, 1])
  print("Check with first pair: ",w[0] * v[:,0], " Should equal: ", matmul(A, v[:,0]))
  print("Check with second pair: ",w[1] * v[:,1], " Should equal: ", matmul(A, v[:,1]))
main()