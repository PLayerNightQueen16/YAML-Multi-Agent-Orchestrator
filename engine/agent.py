class Agent:
    def __init__(self, agent_id, role, goal, tools=None):
        self.id = agent_id
        self.role = role
        self.goal = goal
        self.tools = tools or []

    def run(self, context):
        """
        Simulate agent execution.
        The agent receives shared context and produces an output.
        """
        context_summary = ""

        if context:
            context_summary = "\n".join(
                f"- From {k}: {v}" for k, v in context.items()
            )

        output = (
            f"[{self.role} | {self.id}]\n"
            f"Goal: {self.goal}\n"
        )

        if context_summary:
            output += f"Context received:\n{context_summary}\n"

        # Tool execution (MCP-style support)
        if self.tools:
            tool_results = self.run_tools()
            output += "Tools used:\n"
            for result in tool_results:
                output += f"- {result}\n"

        output += "Result: Task completed successfully."
        return output

    def run_tools(self):
        """
        Simulate tool execution.
        """
        results = []
        for tool in self.tools:
            if tool == "python":
                results.append("Python tool executed successfully")
            elif tool == "web":
                results.append("Web tool invoked")
            else:
                results.append(f"Unknown tool: {tool}")
        return results
