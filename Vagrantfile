Vagrant::Config.run do |config|

  config.vm.define :ci do |ci_config|
    ci_config.vm.box 'precise'
    ci_config.vm.forward_port 80, 8001
    ci_config.vm.provision :chef_solo do |chef|
      chef.cookbooks_path = ["cookbooks"]
      chef.add_recipe("jenkins")
      chef.add_recipe("mattjmorrison")
      chef.add_recipe("nodejs")
      chef.add_recipe("jscoverage")
    end
  end

  config.vm.define :dependencies do |dep_config|
    dep_config.vm.box 'precise'
    dep_config.vm.forward_port 80, 8002
    ci_config.vm.provision :chef_solo do |chef|
      chef.cookbooks_path = ["cookbooks"]
      chef.add_recipe("mattjmorrison")
    end
  end

end