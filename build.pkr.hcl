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

source "googlecompute" "windows-examples" {
  project_id = var.project_id
  source_image = "windows-server-2019-dc-v20200813"
  disk_size = 50
  communicator = "winrm"
  winrm_username = "packer_user"
  winrm_insecure = true
  winrm_use_ssl = true
  metadata = {
    windows-startup-script-cmd = "winrm quickconfig -quiet & net user /add packer_user & net localgroup administrators packer_user /add & winrm set winrm/config/service/auth @{Basic=\"true\"}"
  }
  zone = var.zone
}

build {
  sources = ["sources.googlecompute.windows-examples"]

  provisioner "powershell" {
    inline = [
        "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))",
        "choco feature enable -n allowGlobalConfirmation",
        "choco install python --version=3.10.0",
    ]
}
}