.PHONY: minikube docker kubectl-db kubectl-web port-forward execall

execall: minikube docker kubectl-db kubectl-web port-forward
docker:
	docker build -t task5 .
minikube:
	minikube start
	minikube image load task5
kubectl-db:
	kubectl apply -f yamls/db-secrets.yaml
	kubectl apply -f yamls/db-pv.yaml
	kubectl apply -f yamls/db-pvc.yaml
	kubectl apply -f yamls/db-deployment.yaml
	kubectl apply -f yamls/db-service.yaml
kubectl-web:
	kubectl apply -f yamls/task5-deployment.yaml
	kubectl apply -f yamls/task5-service.yaml
port-forward:
	kubectl port-forward service/task5-service 8080:80
