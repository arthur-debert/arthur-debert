
Vagrant::Config.run do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "precise64"
  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url =   "http://files.vagrantup.com/precise64.box"
  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # create for redis and postgres

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network :private_network, ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network :public_network

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
end
Vagrant.configure("2") do |config|
  config.vm.network :forwarded_port, guest: 4001, host: 3000
  config.vm.synced_folder ".", "/var/www/source/"
  config.vm.synced_folder "../arthur-debert.github.io", "/var/www/build/"
  # synced folders will always be set to vagrant:vagrant , and it can't be changed
  # from inside the vm, this is hackish, but well....
  config.vm.provider :virtualbox do |vb|
  config.vm.provision "docker", images: ["ubuntu"]
      vb.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/app", "1"]
      vb.customize ["modifyvm", :id, "--memory", 2024]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]

  end
  
end
  
  


