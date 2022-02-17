variable "project_id" {
  type = string
}

variable "zone" {
    type = string
}

packer {
  required_plugins {
    googlecompute = {
      version = ">= 0.0.1"
      source = "github.com/hashicorp/googlecompute"
    }
  }
}

source "googlecompute" "basic-examples" {
  project_id = var.project_id
  source_image = "debian-9-stretch-v20200805"
  ssh_username = "packer"
  zone = var.zone
}

build {
  sources = ["sources.googlecompute.basic-examples"]

  provisioner "shell" {
    inline = [
        "echo Retrieving latest code",
        "gsutil cp gs://pybuck-1/example.py ."
    ]
}
}

