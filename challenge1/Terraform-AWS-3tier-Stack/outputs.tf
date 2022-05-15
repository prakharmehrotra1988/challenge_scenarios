# Getting the DNS of load balancer and using this DNS as CNAME for your domain
output "lb_dns_name" {
  description = "The DNS name of the load balancer"
  value       = aws_lb.external-alb.dns_name
}