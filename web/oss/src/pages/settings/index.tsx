import {useEffect, useMemo} from "react"

import {Typography} from "antd"
import dynamic from "next/dynamic"
import {useRouter} from "next/router"

import ProtectedRoute from "@/oss/components/ProtectedRoute/ProtectedRoute"
import {useProjectData} from "@/oss/contexts/project.context"
import {useQueryParam} from "@/oss/hooks/useQuery"

const Secrets = dynamic(() => import("@/oss/components/pages/settings/Secrets/Secrets"), {
    ssr: false,
})
const WorkspaceManage = dynamic(
    () => import("@/oss/components/pages/settings/WorkspaceManage/WorkspaceManage"),
    {ssr: false},
)
const APIKeys = dynamic(() => import("@/oss/components/pages/settings/APIKeys/APIKeys"), {
    ssr: false,
})
const Billing = dynamic(() => import("@/oss/components/pages/settings/Billing"), {
    ssr: false,
})

const Settings: React.FC = () => {
    const [tab] = useQueryParam("tab", "workspace", "replace")
    const router = useRouter()
    const {project} = useProjectData()

    useEffect(() => {
        if (project?.is_demo) {
            router.push("/apps")
        }
    }, [project, router])

    const {content, title} = useMemo(() => {
        switch (tab) {
            case "secrets":
                return {content: <Secrets />, title: "Model Hub"}
            case "apiKeys":
                return {content: <APIKeys />, title: "API Keys"}
            case "billing":
                return {content: <Billing />, title: "Usage & Billing"}
            default:
                return {content: <WorkspaceManage />, title: "Workspace"}
        }
    }, [tab])

    return (
        <main className="flex flex-col gap-4">
            <Typography.Title level={4} className="!font-medium !m-0">
                {title}
            </Typography.Title>
            {content}
        </main>
    )
}

export default () => (
    <ProtectedRoute>
        <Settings />
    </ProtectedRoute>
)
