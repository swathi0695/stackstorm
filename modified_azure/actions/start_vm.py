from lib.base import AzureBaseAction

class StartVM(AzureBaseAction):

	def run(self, group_name, vm_name):
	
		credentials, subscription_id = self.get_credentials()
		resource_client = ResourceManagementClient(credentials, subscription_id)
		compute_client = ComputeManagementClient(credentials, subscription_id)
		network_client = NetworkManagementClient(credentials, subscription_id)
		
		try:
		# Start the VM
			print('\nStart VM')
			async_vm_start = compute_client.virtual_machines.start(
				group_name, vm_name)
			result = {"output" : async_vm_start,"message": vm_name + "VM creation successful"}
		except CloudError:
			result = {"error" : "A VM operation failed:\n" + traceback.format_exc()}
		else:
			result = {"message" : "Start-VM operation completed successfully!"}
		
		return result
