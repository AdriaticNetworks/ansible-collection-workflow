from ansible.module_utils.basic import AnsibleModule

def main():
    input_params = {
        "param1": {"required": True, "type": "str"}
    }

    module = AnsibleModule(argument_spec=input_params)

    module.exit_json(
        "changed": False,
        "status": True,
        "message": f"Input params was" {module.params['param1']}"
    )

if __name__ == "__main__":
    main()